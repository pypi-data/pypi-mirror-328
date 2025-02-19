

from typing import Any, List
from antlr4 import CommonTokenStream, InputStream, Lexer, Token
from dAngr.cli.grammar.antlr.dAngrLexer import dAngrLexer
from dAngr.cli.grammar.antlr.dAngrParser import dAngrParser
from dAngr.cli.grammar.error_listener import ErrorListener
from dAngr.cli.grammar.visitor import dAngrVisitor_
from dAngr.cli.grammar.script import Script
from dAngr.exceptions import ParseError

from dAngr.utils.loggers import AsyncLogger

log = AsyncLogger(__file__)


def logTokens(stream:CommonTokenStream, Parser:type[Any], lexer:Any):
    stream.fill()
    result:List[str] = []
    line = -1
    # print token types and value per line, hence if line number changes, print on new line

    switcher = {
                -1: "EOF",
    }
    if getattr(Parser, "INDENT", None):
        switcher[Parser.INDENT] = "INDENT"
        switcher[Parser.DEDENT] = "DEDENT"

    for token in stream.tokens:
        if token.line != line:
            line = token.line
            result.append(f"{token.line}: ")
        if token.type in switcher:
            token_type = switcher[token.type]
        else:
            token_type = lexer.ruleNames[token.type-1]
        result[-1] +=f"{token_type}({token.text}) "

    log.debug(lambda:"\n".join(result))
    return result

def lex_input(input, Lexer:type[Any]=dAngrLexer, Parser:type[Any]=dAngrParser):
    input_stream = InputStream(input)
    lexer = Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    error_listener = ErrorListener("Parse error")
    lexer.addErrorListener(error_listener)
    if error_listener._errors:
        raise ParseError("\n".join([e for e in error_listener.errors]))
    return logTokens(stream, Parser, lexer)

def validate_input(input:str):
    input_stream = InputStream(input)
    lexer = dAngrLexer(input_stream)
    lexer.removeErrorListeners()
    syntax_error_listener = ErrorListener("Syntax error")
    lexer.addErrorListener(syntax_error_listener)
    stream = CommonTokenStream(lexer)
    parser = dAngrParser(stream)
    error_listener = ErrorListener("Parse error")
    parser.removeErrorListeners()  # Remove default console error listener
    parser.addErrorListener(error_listener)
    tree = parser.script()
    if syntax_error_listener._errors:
        return str(syntax_error_listener.errors[0])
    if error_listener._errors:
       return str(error_listener.errors[0])
    if not tree:
        return "No tree generated"
    

def parse_input(input:str, debugger, Lexer:type[Any]=dAngrLexer, Parser:type[Any] = dAngrParser, Visitor:type[Any]|None = dAngrVisitor_)-> Script:
    input_stream = InputStream(input)
    lexer = Lexer(input_stream)
    lexer.removeErrorListeners()
    syntax_error_listener = ErrorListener("Syntax error")
    lexer.addErrorListener(syntax_error_listener)
    stream = CommonTokenStream(lexer)
    logTokens(stream, Parser, lexer)
    parser = Parser(stream)
    error_listener = ErrorListener("Parse error")
    parser.removeErrorListeners()  # Remove default console error listener
    parser.addErrorListener(error_listener)
    tree = parser.script()
    if syntax_error_listener._errors:
        raise ParseError("\n".join([e for e in syntax_error_listener.errors]))
    if error_listener._errors:
        raise ParseError("\n".join([e for e in error_listener.errors]))
    if not tree:
        raise ParseError("No tree generated")
    log.debug(lambda:tree.toStringTree(recog=parser))
    
    if not Visitor:
        raise ParseError("No visitor provided")
    visitor = Visitor(debugger)
    return visitor.visit(tree)
