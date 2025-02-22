from hydro.md5 import Cracker
from hydro.logging import log
from hydro.files import get_hash, get_wordlist

import click
import rich


@click.command()
@click.argument("hash", required=True)
@click.argument("wordlist", required=True)
def cli(hash: str, wordlist: str):
    try:
        hash = get_hash(hash)
        wordlist = get_wordlist(wordlist)
        cracker = Cracker(hash, wordlist)
        result = cracker.crack()
        if result:
            rich.print(f"[bold green]Success![/bold green] {hash}:{result}")
        else:
            log.info("Hash could not be cracked, maybe try a different wordlist")
    except Exception as e:
        log.error(e)
