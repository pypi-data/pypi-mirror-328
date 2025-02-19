from dAngr.cli.command_line_debugger import CommandLineDebugger
from dAngr.cli.cli_connection import CliConnection


import pytest


import os
from unittest.mock import Mock


class TestMemoryCommands:
    old_dir = os.getcwd()

    def setup_method(self):
        os.chdir(os.path.dirname(__file__))

    def teardown_method(self):
        os.chdir(self.old_dir)


    @pytest.fixture
    def conn(self):
        c = CliConnection()
        c.send_result = Mock()
        c.send_info = Mock()
        c.send_error = Mock()
        return c

    @pytest.fixture
    def dbg(self,conn):
        dbg = CommandLineDebugger(conn)
        assert dbg.handle("load example")
        assert dbg.handle("unconstrained_fill False")
        assert dbg.handle("add_breakpoint 0x400566")
        assert dbg.handle("set_function_prototype 'int processMessage(char*, int, char**)'")
        assert dbg.handle("set_function_call 'processMessage(\"abc\",2,b\"0000000000\")'")
        conn.send_result = Mock()
        conn.send_info = Mock()
        conn.send_error = Mock()

        return dbg

    
    def test_get_memory(self, dbg, conn):
        assert dbg.handle("m = memory.get_memory 0x1000 3")
        assert dbg.handle("evaluate m")
        assert "b'abc'" == str(conn.send_result.call_args[0][0])
    
    # 
    # def test_get_int_memory(self, dbg, conn):
    #     assert dbg.handle("get_int_memory 0x3000 3")
    #     assert r == True
    #     assert "Memory at 0x2000: 0 (int)" == str(conn.send_info.call_args[0][0])
    
    def test_get_string_memory(self, dbg, conn):
        assert dbg.handle("get_memory_string 0x1000")
        assert "abc" == str(conn.send_result.call_args[0][0])
    
    def test_get_register(self, dbg, conn):
        assert dbg.handle("reg = get_register ip")
        assert dbg.handle("cast_to (evaluate reg) address")
        assert "0x40054d" == str(conn.send_result.call_args[0][0])

    
    def test_get_register_invalid(self, dbg, conn):
        assert dbg.handle("get_register invalid",False)
        assert "Register 'invalid' not found." == str(conn.send_error.call_args[0][0])
    
    
    def test_get_register_invalid_args(self, dbg, conn):
        assert dbg.handle("get_register",False)
        assert "missing a required argument: 'name'" == str(conn.send_error.call_args[0][0])
    
    
    def test_list_registers(self, dbg, conn):
        assert dbg.handle("list_registers")
        assert "Register rax " in str(conn.send_result.call_args[0][0])

    
    def test_set_register(self, dbg, conn):
        assert dbg.handle("set_register ip 0x4e")
        assert "Register ip: 0x4e." == str(conn.send_info.call_args[0][0])

    
    def test_set_memory_int(self, dbg, conn):
        assert dbg.handle("set_memory 0x1000 0x61")
        assert "Memory at 0x1000: 97." == str(conn.send_info.call_args[0][0])
        
    
    def test_set_memory_str(self, dbg, conn):
        assert dbg.handle("set_memory 0x1000 'abs'")
        assert "Memory at 0x1000: abs." == str(conn.send_info.call_args[0][0])

    
    def test_set_memory_bytes(self, dbg, conn):
        assert dbg.handle("set_memory 0x1000 b'1234'")
        assert "Memory at 0x1000: b'1234'." == str(conn.send_info.call_args[0][0])

    
    def test_unconstrained_fill_memory(self, dbg, conn):
        assert dbg.handle("unconstrained_fill")
        assert "Fill with zeros." == str(conn.send_info.call_args[0][0])

        assert dbg.handle("unconstrained_fill True")
        assert "Fill with symbols." == str(conn.send_info.call_args[0][0])
            
    
    def test_get_return_value(self, dbg, conn):
        assert dbg.handle("run")
        assert dbg.handle("run")
        assert dbg.handle("get_return_value")
        assert "6" == str(conn.send_result.call_args[0][0])