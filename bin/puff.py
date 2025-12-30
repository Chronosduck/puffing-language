#!/usr/bin/env python3
"""
Puffing Language Interpreter
Entry point for running .pf files or starting REPL
No main() function - uses class-based runner pattern
"""

import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.lexer import Lexer
from src.parser import Parser
from src.interpreter import Interpreter
from src.errors import PuffingError


class PuffingRunner:
    """Main runner for Puffing Language"""
    
    def __init__(self):
        self.interpreter = Interpreter()
        self.version = "0.1.0"
    
    def run_source(self, code):
        """Execute Puffing source code"""
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        parser = Parser(tokens)
        ast = parser.parse()
        self.interpreter.run(ast)
    
    def run_file(self, filename):
        """Run a .pf file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.run_source(f.read())
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            sys.exit(1)
        except PuffingError as e:
            print(f"Error: {e}")
            sys.exit(1)
        except Exception as e:
            print(f"Unexpected error: {e}")
            sys.exit(1)
    
    def repl(self):
        """Start interactive REPL"""
        print("╔════════════════════════════════════╗")
        print(f"║   Puffing Language v{self.version}          ║")
        print("║   Type 'exit' or Ctrl+C to quit   ║")
        print("╚════════════════════════════════════╝")
        print()
        
        while True:
            try:
                code = input(">>> ")
                
                if code.strip() in ('exit', 'quit'):
                    print("Goodbye!")
                    break
                    
                if not code.strip():
                    continue
                    
                self.run_source(code)
                
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except PuffingError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
    
    def start(self):
        """Start the runner based on command-line arguments"""
        if len(sys.argv) > 1:
            self.run_file(sys.argv[1])
        else:
            self.repl()


# Create instance and run immediately (NO main function!)
runner = PuffingRunner()
runner.start()