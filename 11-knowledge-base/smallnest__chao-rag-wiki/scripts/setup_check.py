"""First-run preflight for chao-rag-wiki.

Checks everything the skill needs before a build, against whatever embedding
provider is configured (OpenAI-compatible endpoint via RAG_EMBED_* env vars;
defaults to Qianfan). Prints an ordered report so the agent can guide the user
through whatever is missing:

  1. venv + core deps (turbovec, numpy, requests)
  2. an embedding API key is resolvable
  3. the configured endpoint is reachable + returns the expected dimension

Exit code 0 = ready to build. Non-zero = something needs fixing; the stderr
report says what and how. Run with the skill's venv python.
"""
import os
import sys

OK = "[OK]"
BAD = "[!!]"


def main():
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    problems = []

    # 1. core deps -----------------------------------------------------------
    missing = []
    for mod in ("turbovec", "numpy", "requests"):
        try:
            __import__(mod)
        except ImportError:
            missing.append(mod)
    if missing:
        print(f"{BAD} venv missing packages: {', '.join(missing)}")
        print("     fix: <skill>/.venv/bin/pip install -q turbovec numpy requests")
        problems.append("deps")
        # Without requests we can't probe; report what we can and stop early.
        print("\nNOT READY — install deps, then re-run this check.")
        sys.exit(1)
    print(f"{OK} core deps installed (turbovec, numpy, requests)")

    # Pull resolved config from the embed module (single source of truth).
    import embed
    base_url, model, dim = embed.BASE_URL, embed.MODEL, embed.DIM
    print(f"     provider: base_url={base_url}  model={model}  dim={dim}")

    # 2. API key -------------------------------------------------------------
    key = None
    for var in ("RAG_EMBED_API_KEY", "QIANFAN_API_KEY", "OPENAI_API_KEY"):
        if os.environ.get(var):
            key = os.environ[var]
            print(f"{OK} API key found in {var} ({key[:6]}…{key[-4:]})")
            break
    if not key:
        print(f"{BAD} no embedding API key set")
        print("     This skill embeds text via an online OpenAI-compatible API.")
        print("     Default provider is Qianfan (model bge-large-zh). Set a key:")
        print('       export RAG_EMBED_API_KEY="..."   # or QIANFAN_API_KEY for Qianfan')
        print("     To use another provider, also set the endpoint, e.g. OpenAI:")
        print('       export RAG_EMBED_BASE_URL="https://api.openai.com/v1"')
        print('       export RAG_EMBED_MODEL="text-embedding-3-small"')
        print('       export RAG_EMBED_DIM="1536"')
        print("     (add to your shell profile so it persists; never hard-code it.)")
        problems.append("key")

    # 3. live connectivity + dimension check --------------------------------
    if key:
        try:
            got = len(embed.embed(["连接测试 connectivity check"])[0])
            if got != dim:
                print(f"{BAD} model {model} returned dim={got}, expected {dim}. "
                      f"Set RAG_EMBED_DIM={got} (and rebuild).")
                problems.append("dim")
            else:
                print(f"{OK} endpoint reachable — {model} @ {base_url}, dim={got}")
        except SystemExit as e:
            # embed.embed() calls sys.exit on hard failure; surface its message.
            print(f"{BAD} embedding call failed: {e}")
            print("     Check the key, model name, and network to the endpoint.")
            problems.append("api")
        except Exception as e:  # noqa: BLE001
            print(f"{BAD} could not reach embedding endpoint: {e}")
            problems.append("api")

    print()
    if problems:
        print(f"NOT READY — resolve the {len(problems)} item(s) above, "
              "then re-run this check.")
        sys.exit(1)
    print("READY — embedding is configured. You can build the index now.")


if __name__ == "__main__":
    main()
