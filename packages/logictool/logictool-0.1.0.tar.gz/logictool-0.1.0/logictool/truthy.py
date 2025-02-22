#!/usr/bin/env python3

import argparse
from itertools import product
import re
import subprocess
import platform
import sys

def parse_expression(expression):
    """Parse a Boolean expression into function name, expression, and variables."""
    expression = expression.replace(" ", "")
    expression = re.sub(r"([A-Za-z])'", r"/\1", expression)
    expression = re.sub(r"([A-Za-z])’", r"/\1", expression)
    expression = re.sub(r"!([A-Za-z])", r"/\1", expression)

    if "=" in expression:
        sides = expression.split("=")
        if len(sides) != 2:
            raise ValueError("Expression can only contain one '='")
        function_name = sides[0].strip()
        expression = sides[1].strip()
    else:
        function_name = "Result"
        expression = expression.strip()
    variables = sorted(set(re.findall(r'[A-Za-z]', expression)))
    return function_name, expression, variables

def validate_vars(vars_str, expression_vars):
    """Validate the variable order string against expression variables."""
    if len(vars_str) != len(set(vars_str)):
        raise ValueError("Variable order string contains duplicate variables")
    missing_vars = set(expression_vars) - set(vars_str)
    if missing_vars:
        raise ValueError(f"Variable order string missing variables from expression: {', '.join(sorted(missing_vars))}")

def evaluate_boolean(expression, var_dict):
    """Evaluate a Boolean expression given a dictionary of variable values."""
    while '(' in expression:
        match = re.search(r'\(([^()]+)\)', expression)
        if not match:
            break
        inner_expr = match.group(1)
        result = evaluate_boolean(inner_expr, var_dict)
        expression = expression[:match.start()] + str(int(result)) + expression[match.end():]
    while '/' in expression:
        match = re.search(r'/([A-Za-z0-1]+)', expression)
        if not match:
            break
        var = match.group(1)
        value = int(not (var_dict[var] if var in var_dict else int(var)))
        expression = expression[:match.start()] + str(value) + expression[match.end():]
    expression = re.sub(r'([A-Za-z0-1])([A-Za-z0-1\(])', r'\1*\2', expression)
    for var, val in var_dict.items():
        expression = expression.replace(var, str(int(val)))
    terms = expression.split('+')
    result = False
    for term in terms:
        factors = term.split('*')
        term_result = True
        for factor in factors:
            if factor.strip():
                term_result = term_result and bool(int(factor))
        result = result or term_result
    return result

def set_clipboard_html(html_content, function: str = None):
    """Copy HTML content to the clipboard for pasting into Word."""
    if function is None:
        formatted_html = (
            '<html xmlns:o="urn:schemas-microsoft-com:office:office" '
            'xmlns:x="urn:schemas-microsoft-com:office:excel" '
            'xmlns="http://www.w3.org/TR/REC-html40">'
            '<head><meta charset="utf-8"></head>'
            '<body>'
            '<table style="border-collapse:collapse; border:1px solid black">'
            f'{html_content}'
            '</table>'
            '</body>'
            '</html>'
        )
    else:
        formatted_html = (
            '<html xmlns:o="urn:schemas-microsoft-com:office:office" '
            'xmlns:x="urn:schemas-microsoft-com:office:excel" '
            'xmlns="http://www.w3.org/TR/REC-html40">'
            '<head><meta charset="utf-8"></head>'
            '<body>'
            f'<p>{function}</p>'
            '<table style="border-collapse:collapse; border:1px solid black">'
            f'{html_content}'
            '</table>'
            '</body>'
            '</html>'
        )
    if platform.system() == 'Linux':
        try:
            p = subprocess.Popen(['xclip', '-selection', 'clipboard', '-t', 'text/html', '-i'], 
                               stdin=subprocess.PIPE)
            p.communicate(input=formatted_html.encode())
        except FileNotFoundError:
            print("Error: xclip not installed.", file=sys.stderr)
            return False
    elif platform.system() == 'Windows':
        try:
            p = subprocess.Popen(['clip'], stdin=subprocess.PIPE)
            p.communicate(input=formatted_html.encode())
        except:
            print("Error setting clipboard on Windows", file=sys.stderr)
            return False
    elif platform.system() == "Darwin":
        try:
            p1 = subprocess.Popen(
                ["textutil", "-stdin", "-format", "html", "-convert", "rtf", "-stdout"],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE
            )
            p2 = subprocess.Popen(["pbcopy"], stdin=p1.stdout)
            p1.communicate(input=formatted_html.encode())
        except:
            print("Error setting clipboard on MacOS", file=sys.stderr)
            return False
    else:
        print(f"Unsupported platform: {platform.system()}", file=sys.stderr)
        return False
    return True

def generate_truth_table(function_name, expression, ordered_vars, var_activations=None, output_format='normal', function=None):
    """Generate a truth table in the specified format."""
    physical_combinations = list(product(['L', 'H'], repeat=len(ordered_vars)))
    
    if output_format == 'normal':
        if function: print(function_name, "=", expression)
    
        # Normal text table output
        if var_activations:
            header_parts = []
            for var in ordered_vars:
                activation = var_activations.get(var, 'H')
                header_parts.append(f"{var}({activation})")
                if activation == 'L':
                    header_parts.append(f"{var} (H)")
            header = ' '.join(f'{part:^{7}}' for part in header_parts)
        else:
            header = ' '.join(f'{var:^5}' for var in ordered_vars)
        print(f'{header} | {function_name}')
        separator = '-' * (len(header)+1) + '|' + '-' * 5
        print(separator)
        
        for physical_values in physical_combinations:
            logical_values = {}
            h_values = {}
            for var, phys in zip(ordered_vars, physical_values):
                activation = var_activations.get(var, 'H') if var_activations else 'H'
                logical = (phys == 'H') if activation == 'H' else (phys == 'L')
                logical_values[var] = logical
                h_values[var] = 'H' if logical else 'L'
            
            eval_dict = {var: (h_values[var] == 'H') for var in ordered_vars}
            result = evaluate_boolean(expression, eval_dict)
            output = 'H' if result else 'L'
            
            if var_activations:
                row_parts = []
                for var, phys in zip(ordered_vars, physical_values):
                    row_parts.append(f"{phys:^7}")
                    if var_activations.get(var, 'H') == 'L':
                        row_parts.append(f"{h_values[var]:^7}")
                row_str = ' '.join(row_parts)
            else:
                row_parts = [f"{('1' if logical_values[var] else '0'):^5}" for var in ordered_vars]
                row_str = ' '.join(row_parts)
                output = '1' if result else '0'
            print(f'{row_str} |  {output}')
            
    elif output_format == 'inline':
        if function: print(function_name, "=", expression)

        # Single-line result string
        results = ''
        for physical_values in physical_combinations:
            logical_values = {}
            h_values = {}
            for var, phys in zip(ordered_vars, physical_values):
                activation = var_activations.get(var, 'H') if var_activations else 'H'
                logical = (phys == 'H') if activation == 'H' else (phys == 'L')
                logical_values[var] = logical
                h_values[var] = 'H' if logical else 'L'
            eval_dict = {var: (h_values[var] == 'H') for var in ordered_vars}
            result = evaluate_boolean(expression, eval_dict)
            results += ('H' if result else 'L') if var_activations else '1' if result else '0'
        print(results, end='')
        
    elif output_format == 'word':
        # HTML table for Word
        html = ""
        if var_activations:
            header_parts = []
            for var in ordered_vars:
                activation = var_activations.get(var, 'H')
                header_parts.append(f"{var}({activation})")
                if activation == 'L':
                    header_parts.append(f"{var} (H)")
            html += "<tr style='border:1px solid black'>\n"
            for part in header_parts:
                html += f"<td style='border:1px solid black; border-bottom: 3px solid black; padding:4px; background-color: lightgray'>{part}</td>\n"
            html += f"<td style='border:1px solid black; border-left: 3px solid black; border-bottom: 3px solid black; padding:4px; background-color: lightgray'>{function_name}</td>\n</tr>\n"
            for physical_values in physical_combinations:
                logical_values = {var: (phys == 'H') if var_activations.get(var, 'H') == 'H' else (phys == 'L') for var, phys in zip(ordered_vars, physical_values)}
                h_values = {var: 'H' if logical_values[var] else 'L' for var in ordered_vars}
                eval_dict = {var: (h_values[var] == 'H') for var in ordered_vars}
                result = evaluate_boolean(expression, eval_dict)
                html += "<tr style='border:1px solid black'>\n"
                for var, phys in zip(ordered_vars, physical_values):
                    html += f"<td style='border:1px solid black; padding:4px'>{phys}</td>\n"
                    if var_activations.get(var, 'H') == 'L':
                        html += f"<td style='border:1px solid black; padding:4px'>{h_values[var]}</td>\n"
                html += f"<td style='border:1px solid black; border-left: 3px solid black; padding:4px'>{'H' if result else 'L'}</td>\n</tr>\n"
        else:
            html += "<tr style='border:1px solid black'>\n"
            for var in ordered_vars:
                html += f"<td style='border:1px solid black; border-bottom: 3px solid black; padding:4px; background-color: lightgray'>{var}</td>\n"
            html += f"<td style='border:1px solid black; border-left: 3px solid black; border-bottom: 3px solid black; padding:4px; background-color: lightgray'>{function_name}</td>\n</tr>\n"
            for physical_values in physical_combinations:
                logical_values = {var: (phys == 'H') for var, phys in zip(ordered_vars, physical_values)}
                result = evaluate_boolean(expression, logical_values)
                html += "<tr style='border:1px solid black'>\n"
                for log_val in logical_values.values():
                    html += f"<td style='border:1px solid black; padding:4px'>{'1' if log_val else '0'}</td>\n"
                html += f"<td style='border:1px solid black; border-left: 3px solid black; padding:4px'>{'1' if result else '0'}</td>\n</tr>\n"
        if function:
            set_clipboard_html(html, f"{function_name} = {expression}")
        else:
            set_clipboard_html(html)

def main():
    """Parse arguments and generate the truth table."""
    parser = argparse.ArgumentParser(description='Generate truth table for boolean expression')
    parser.add_argument('expression', nargs='?', default=None,
                        help='Boolean expression (e.g., "F = A*B + !C" or "A*B + C\'" or "A*B + /C")')
    parser.add_argument('--vars', '-v',
                        help='Specify the order and additional variables (e.g., "BACD")')
    parser.add_argument('--activations', '-a',
                        help='Specify activation levels for variables (e.g., "HLHL")')
    parser.add_argument('--function', '-f', action='store_true',
                        help='Print the function before the truth table output')
    format_group = parser.add_mutually_exclusive_group()
    format_group.add_argument('--inline', '-i', action='store_true',
                              help='Output only the result column as a single line')
    format_group.add_argument('--word', '-w', action='store_true',
                              help='Copy Word table formatting to clipboard')
    args = parser.parse_args()

    try:
        if args.expression is None:
            if sys.stdin.isatty():
                parser.print_help()
                return
            args.expression = sys.stdin.read().strip()

        function_name, expression, expr_vars = parse_expression(args.expression)

        if args.vars:
            validate_vars(args.vars, expr_vars)
            ordered_vars = list(args.vars)
        else:
            ordered_vars = expr_vars
            
        if args.activations:
            activations = args.activations.upper()
            if len(activations) != len(ordered_vars):
                raise ValueError("Activations string must have the same length as the number of variables")
            if not all(c in 'HL' for c in activations):
                raise ValueError("Activations string must consist only of 'H' and 'L'")
            var_activations = dict(zip(ordered_vars, activations))
        else:
            var_activations = None
            
        output_format = 'inline' if args.inline else 'word' if args.word else 'normal'

        generate_truth_table(function_name, expression, ordered_vars, var_activations, output_format, args.function)
            
    except Exception as e:
        print(f"Error: {e}")
        raise

if __name__ == "__main__":
    main()