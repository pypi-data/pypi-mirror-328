import sys
from collections import deque
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

class TimeTravelDebugger:
    def __init__(self, max_steps=1000):
        self.execution_log = deque(maxlen=max_steps)
        self.current_step = -1
        self.breakpoints = set()
        self.last_state = {}

    def trace_calls(self, frame, event, arg):
        """Trace function execution and store changed variables."""
        if event == "line":
            current_vars = frame.f_locals
            changed_vars = {k: v for k, v in current_vars.items() if self.last_state.get(k) != v}

            if changed_vars:
                self.execution_log.append((frame.f_lineno, changed_vars, frame.f_code.co_name))
                self.current_step += 1
                self.last_state.update(changed_vars)

            if frame.f_lineno in self.breakpoints:
                console.print(Panel(f"⛔ [bold red]Breakpoint hit at Line {frame.f_lineno} in {frame.f_code.co_name}[/bold red]", title="Debugger"))
                self.debugger_cli()

        return self.trace_calls

    def start_debugging(self, func, *args, **kwargs):
        """Starts tracing execution of a function."""
        sys.settrace(self.trace_calls)
        func(*args, **kwargs)
        sys.settrace(None)

    def step_forward(self):
        """Move forward in execution."""
        if self.current_step < len(self.execution_log) - 1:
            self.current_step += 1
            line, vars_at_step, func = self.execution_log[self.current_step]

            table = Table(title=f"▶️ [bold green]Step Forward: Line {line} in {func}[/bold green]")
            table.add_column("Variable", style="cyan")
            table.add_column("Value", style="magenta")

            for var, value in vars_at_step.items():
                table.add_row(var, str(value))

            console.print(table)
        else:
            console.print("[bold red]🚫 No further steps available![/bold red]")

    def step_backward(self):
        """Rewind execution by restoring previous variable states."""
        if self.current_step > 0:
            self.current_step -= 1
            line, vars_at_step, func = self.execution_log[self.current_step]

            table = Table(title=f"⏪ [bold yellow]Step Backward: Line {line} in {func}[/bold yellow]")
            table.add_column("Variable", style="cyan")
            table.add_column("Restored Value", style="magenta")

            for var, value in vars_at_step.items():
                table.add_row(var, str(value))

            console.print(table)
        else:
            console.print("[bold red]🚫 Cannot rewind further![/bold red]")

    def debugger_cli(self):
        """Interactive CLI with better visuals."""
        while True:
            console.print("\n[bold blue]Debugger Command (f: forward, b: backward, q: quit):[/bold blue]", end=" ")
            command = input().strip().lower()
            if command == "f":
                self.step_forward()
            elif command == "b":
                self.step_backward()
            elif command == "q":
                console.print("[bold green]Exiting Debugger.[/bold green]")
                break
            else:
                console.print("[bold red]Invalid command![/bold red]")
