import re
import collections
import runpod
import tiktoken


# ─────────────────────────────────────────────
# BPE helper functions
# ─────────────────────────────────────────────

def get_vocab(text):
      vocab = collections.defaultdict(int)
      for word in text.strip().split():
                vocab[' '.join(list(word)) + ' </w>'] += 1
            return vocab


def get_stats(vocab):
      pairs = collections.defaultdict(int)
    for word, freq in vocab.items():
              symbols = word.split()
              for i in range(len(symbols) - 1):
                            pairs[(symbols[i], symbols[i + 1])] += freq
                    return pairs


def merge_vocab(pair, v_in):
      v_out = {}
    bigram = re.escape(' '.join(pair))
    p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
    for word in v_in:
              w_out = p.sub(''.join(pair), word)
        v_out[w_out] = v_in[word]
    return v_out


def get_tokens_from_vocab(vocab):
      tokens = collections.defaultdict(int)
    for word, freq in vocab.items():
              word_tokens = word.split()
        for token in word_tokens:
                      tokens[token] += freq
              return tokens


def run_bpe(text, num_merges):
      vocab = get_vocab(text)
    for i in range(num_merges):
              pairs = get_stats(vocab)
        if not pairs:
                      break
                  best = max(pairs, key=pairs.get)
        vocab = merge_vocab(best, vocab)
    tokens = get_tokens_from_vocab(vocab)
    return vocab, tokens


def compute_compression_ratio(text, num_merges):
      original_chars = len(text.replace(' ', ''))
    init_vocab = get_vocab(text)
    base_vocab_size = len(set(ch for word in init_vocab for ch in word.split()))
    final_vocab_size = base_vocab_size + num_merges
    vocab, tokens = run_bpe(text, num_merges)
    total_tokens = sum(tokens[tok] for tok in tokens)
    ratio = original_chars / total_tokens if total_tokens > 0 else 1.0
    return ratio, base_vocab_size, final_vocab_size


def tiktoken_compression_ratio(text, encoding_name):
      enc = tiktoken.get_encoding(encoding_name)
    tokens = enc.encode(text)
    ratio = len(text) / len(tokens) if len(tokens) > 0 else 1.0
    return ratio


# ─────────────────────────────────────────────
# RunPod handler
# ─────────────────────────────────────────────

def handler(job):
      """
          RunPod serverless handler for BPE compression ratio computation.

              Expected input (job["input"]):
                  {
                          "text": "<your input text>",
                                  "num_merges": 200,              # optional, default 200
                                          "tiktoken_model": "gpt2"        # optional: "gpt2", "cl100k_base", or null
                                              }

                                                  Returns:
                                                      {
                                                              "bpe_compression_ratio": float,
                                                                      "base_vocab_size": int,
                                                                              "final_vocab_size": int,
                                                                                      "tiktoken_compression_ratio": float or null
                                                                                          }
                                                                                              """
    job_input = job["input"]

    text = job_input.get("text", "")
    if not text:
              return {"error": "No text provided. Please pass 'text' in the input."}

    num_merges = int(job_input.get("num_merges", 200))
    tiktoken_model = job_input.get("tiktoken_model", None)

    # BPE compression ratio
    bpe_ratio, base_vocab, final_vocab = compute_compression_ratio(text, num_merges)

    result = {
              "bpe_compression_ratio": round(bpe_ratio, 4),
              "base_vocab_size": base_vocab,
              "final_vocab_size": final_vocab,
    }

    # Optional tiktoken comparison
    if tiktoken_model:
              try:
                            tt_ratio = tiktoken_compression_ratio(text, tiktoken_model)
                            result["tiktoken_compression_ratio"] = round(tt_ratio, 4)
                            result["tiktoken_model"] = tiktoken_model
except Exception as e:
            result["tiktoken_error"] = str(e)

    return result


if __name__ == "__main__":
      runpod.serverless.start({"handler": handler})
