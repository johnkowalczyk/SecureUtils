import click
from . import base_encodings, hash_utils, phonetic

@click.group()
def main():
    """SecureUtils: Encoding & Hashing Toolbox"""
    pass

@main.group()
def encode():
    pass

@encode.command()
@click.argument('text')
def base64(text):
    click.echo(base_encodings.encode_base64(text))

@encode.command()
@click.argument('text')
def base32(text):
    click.echo(base_encodings.encode_base32(text))

@encode.command()
@click.argument('text')
def hex(text):
    click.echo(base_encodings.encode_hex(text))

@main.command()
@click.option('--alg', type=click.Choice(['md5', 'sha1', 'sha256', 'sha512']), default='sha256')
@click.argument('text')
def hash(alg, text):
    click.echo(hash_utils.hash_text(text, alg))

@main.group()
def phonetic_cmd():
    """Phonetic encoding commands"""
    pass

@phonetic_cmd.command()
@click.argument('word')
def soundex(word):
    click.echo(phonetic.soundex_encode(word))

@phonetic_cmd.command()
@click.argument('word')
def metaphone(word):
    click.echo(phonetic.metaphone_encode(word))

@phonetic_cmd.command()
@click.argument('word')
def double(word):
    click.echo(phonetic.double_metaphone_primary(word))

@phonetic_cmd.command()
@click.argument('word')
def refined(word):
    click.echo(phonetic.refined_soundex_encode(word))
