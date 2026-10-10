class Delimiter:
    @staticmethod
    def str_split(s: str | None, delim: str) -> list[str] | None:
        if s is None:
            return None

        count = 1
        in_quotes = False
        i = 0
        while i < len(s):
            c = s[i]
            if c == '"':
                if in_quotes and i + 1 < len(s) and s[i + 1] == '"':
                    i += 1
                else:
                    in_quotes = not in_quotes
            elif c == delim and not in_quotes:
                count += 1
            i += 1

        if in_quotes:
            return None

        result: list[str] = []
        p = 0
        n = len(s)
        for idx in range(count):
            field: list[str] = []
            in_quotes = False
            while p < n:
                c = s[p]
                if c == '"':
                    if in_quotes and p + 1 < n and s[p + 1] == '"':
                        field.append('"')
                        p += 2
                    else:
                        in_quotes = not in_quotes
                        p += 1
                elif c == delim and not in_quotes:
                    p += 1
                    break
                else:
                    field.append(c)
                    p += 1
            text = "".join(field)
            if idx == count - 1:
                text = text.rstrip("\r\n")
            result.append(text)
        return result
