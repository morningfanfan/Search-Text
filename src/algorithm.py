from collections import defaultdict

SENTENCE_ENDS = ["!", ".", "?"]
SENTENCE_STARTS = ["!", ".", "?"]


class SimpleSearch:

    def __init__(self, f, ngram=2):
        self._content = [line.strip("\n") for line in f.readlines()]

        self._word_index = defaultdict(list)
        self._ngram = ngram
        self._build_index()

    def _build_index(self):
        """
        Build ngram index.
        For each 1gram - ngram word appeared in the document, add their position to a hashmap
        """
        for linum, line_content in enumerate(self._content):
            for colnum in range(len(line_content)):
                for n in range(1, self._ngram+1):
                    if colnum+n >= len(line_content):
                        continue
                    ngram_word = line_content[colnum:colnum+n]
                    self._word_index[ngram_word].append((linum, colnum))

    def search(self, substr):
        """
        Given a substring, search for all the occurrences in the document.
        """
        n = min(len(substr), self._ngram)
        prefix = substr[:n]

        re_dict = {
            "query_text": substr,
            "number_of_occurrences": 0,
            "occurrences": []
        }
        for (linum, colnum) in self._word_index[prefix]:
            line_content = self._content[linum]
            line_content_remain = line_content[colnum:]
            if line_content_remain.startswith(substr):
                re_dict["number_of_occurrences"] += 1
                sent = self._extend_sentence(linum, colnum, colnum+len(substr)-1)
                re_dict["occurrences"].append({
                    "line": linum+1,
                    "start": colnum+1,
                    "end": colnum+len(substr)+1,
                    "in_sentence": sent
                })
        return re_dict

    def _offset(self, line, col, offset):
        """
        Get line number and column number by a offset from current position.
        """
        col += offset

        if offset >= 0:
            while col >= len(self._content[line]):
                if line == len(self._content):
                    raise RuntimeError("Offset overflow of buffer")
                col -= len(self._content[line])
                line += 1
            return line, col
        else:
            while col < 0:
                if line == 0:
                    raise RuntimeError("Offset out of buffer")
                line -= 1
                col += len(self._content[line])

            return line, col

    def _extend_sentence(self, line, start_col, end_col):
        """
        Given a substring location, return the sentence including this substring,
        will search the lines before and after if the sentence is a multi-line sentence
        """
        start_line, start_col = line, start_col
        while True:
            if start_line == 0 and start_col == 0:
                break
            else:
                start_line_, start_col_ = self._offset(start_line, start_col, -1)
                if self._content[start_line_][start_col_] in SENTENCE_STARTS:
                    break
                elif start_col_ < len(self._content[start_line_]) - 1 and self._content[start_line_][start_col_:start_col_+2] == "  ":
                    # For those invalid sentences: no period before the end of line
                    start_line, start_col = start_line_, start_col_ + 2
                    break
                else:
                    start_line, start_col = start_line_, start_col_

        end_line, end_col = line, end_col
        while True:
            if end_line == len(self._content) - 1 and end_col == len(self._content[-1]) - 1:
                break
            else:
                if self._content[end_line][end_col] in SENTENCE_ENDS:
                    break
                else:
                    end_line, end_col = self._offset(end_line, end_col, 1)

        buffer = []
        while start_line < end_line:
            buffer.append(self._content[start_line][start_col:])
            start_line += 1
            start_col = 0
        buffer.append(self._content[start_line][start_col:end_col+1])
        return " ".join(buffer).strip()
