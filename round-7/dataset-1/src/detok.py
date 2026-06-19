#!/usr/bin/env python3
"""Detokenize DocRED/Re-DocRED tokenized `sents` into natural prose while recording
per-(sent_id, token_index) character offsets, so every entity mention's char span in
the reconstructed document is recoverable (mirrors iter-5 data_adapter mark_local)."""
from __future__ import annotations

# punctuation that hugs the PRECEDING token (no space before)
_NO_SPACE_BEFORE = {",", ".", "!", "?", ";", ":", ")", "]", "}", "%",
                    "''", "'", "’", "”", "\"", "...", "…", "/", "-", "–"}
# contraction / clitic tokens that hug the preceding token
_CLITICS = {"'s", "'m", "'re", "'ve", "'ll", "'d", "'t", "n't", "’s", "’re", "’ve",
            "’ll", "’d", "’m", "n’t"}
# tokens after which the NEXT token hugs (no space after) -- opening brackets/quotes
# (hyphen/en-dash hug both sides so intra-word names like 'Antonov-Ovseyenko' rejoin)
_NO_SPACE_AFTER = {"(", "[", "{", "``", "`", "“", "‘", "#", "$", "/", "-", "–"}


def detokenize(sents):
    """sents: list[list[str]]. Returns (text, offsets) where
    offsets[sent_id][tok_idx] = (char_start, char_end) into `text`."""
    out = []          # list of string pieces
    cur = 0           # current char length
    offsets = []      # per-sentence list of (start,end)
    prev_tok = None
    prev_no_space_after = False
    first = True
    for s_id, sent in enumerate(sents):
        sent_off = []
        for t_idx, tok in enumerate(sent):
            tok = "" if tok is None else str(tok)
            # decide separator before this token
            if first:
                sep = ""
            elif prev_no_space_after:
                sep = ""
            elif tok in _NO_SPACE_BEFORE or tok in _CLITICS or tok.startswith("'") and tok in _CLITICS:
                sep = ""
            else:
                sep = " "
            if sep:
                out.append(sep); cur += len(sep)
            start = cur
            out.append(tok); cur += len(tok)
            end = cur
            sent_off.append((start, end))
            prev_tok = tok
            prev_no_space_after = tok in _NO_SPACE_AFTER
            first = False
        offsets.append(sent_off)
    return "".join(out), offsets


def mention_char_span(offsets, sent_id, pos):
    """pos = [tok_start, tok_end) within sentence sent_id -> (char_start, char_end)."""
    so = offsets[sent_id]
    ts, te = pos[0], pos[1]
    if not so:
        return None
    ts = max(0, min(ts, len(so) - 1))
    te_idx = max(0, min(te - 1, len(so) - 1))
    return (so[ts][0], so[te_idx][1])


def sent_char_span(offsets, sent_id):
    so = offsets[sent_id]
    if not so:
        return None
    return (so[0][0], so[-1][1])
