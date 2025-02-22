import io
import tokenize
import token

def transform_code(source):
    """
    Transforms DSL code with 'perchance', 'or perchance', and 'certainly'
    into valid Python using 'if', 'elif', and 'else', respectively.
    """
    source_bytes = source.encode('utf-8')
    tokens = list(tokenize.tokenize(io.BytesIO(source_bytes).readline))
    
    new_tokens = []
    i = 0
    while i < len(tokens):
        current = tokens[i]
        # Look for "or perchance" pattern
        if current.type == token.NAME and current.string == "or":
            if i + 1 < len(tokens):
                next_tok = tokens[i+1]
                if next_tok.type == token.NAME and next_tok.string == "perchance":
                    combined = tokenize.TokenInfo(
                        token.NAME,
                        "elif",
                        current.start,
                        next_tok.end,
                        current.line
                    )
                    new_tokens.append(combined)
                    i += 2
                    continue
        # Replace standalone 'perchance' with 'if'
        if current.type == token.NAME and current.string == "perchance":
            new_tok = tokenize.TokenInfo(
                token.NAME,
                "if",
                current.start,
                current.end,
                current.line
            )
            new_tokens.append(new_tok)
            i += 1
            continue
        # Replace 'certainly' with 'else'
        if current.type == token.NAME and current.string == "certainly":
            new_tok = tokenize.TokenInfo(
                token.NAME,
                "else",
                current.start,
                current.end,
                current.line
            )
            new_tokens.append(new_tok)
            i += 1
            continue
        new_tokens.append(current)
        i += 1

    new_source = tokenize.untokenize(new_tokens)
    if isinstance(new_source, bytes):
        new_source = new_source.decode('utf-8')
    return new_source
