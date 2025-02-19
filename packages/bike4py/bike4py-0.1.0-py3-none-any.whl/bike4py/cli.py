import asyncio
import click
import sys
from typing import Optional
from bike4py.client import CompletionEvent, ContentEvent, LLMClient, StatusEvent
from bike4py.config import load_config
from bike4py.models import ChatCompletionRequest

@click.group()
def cli():
    """Bike4py CLI tool"""
    pass

@cli.command()
@click.option('--base-url', help='Base URL for the service')
@click.option('--refresh-token', help='Refresh token for authentication')
@click.option('--mime-type', help='MIME type of the file')
@click.argument('file')
def upload(
    base_url: Optional[str],
    refresh_token: Optional[str],
    mime_type: Optional[str],
    file: str
):
    """Upload a file to the service"""
    config = load_config()
    
    base_url = base_url or config.get('base_url')
    refresh_token = refresh_token or config.get('refresh_token')
    mime_type = mime_type or 'application/octet-stream'

    async def run():
        async with LLMClient(
            base_url=base_url,
            refresh_token=refresh_token
        ) as client:
            fabfile_id = await client.upload_file(file, mime_type)
            print(fabfile_id)

    asyncio.run(run())

@cli.command()
@click.option('--base-url', help='Base URL for the service')
@click.option('--refresh-token', help='Refresh token for authentication')
@click.option('--notebook-id', help='Notebook ID')
@click.option('--model', default='gpt-4o', help='Model to use')
@click.option('--temperature', type=float, default=0.7, help='Temperature parameter')
@click.option('--stream/--no-stream', is_flag=True, default=True, 
              help='Stream the response as it arrives (--no-stream to wait for complete response)')
@click.option('--verbose', is_flag=True, default=False, help='Verbose output')
@click.option('--attach-files', help='Files to attach to the prompt')
@click.argument('prompt')
def complete(
    base_url: Optional[str],
    refresh_token: Optional[str],
    notebook_id: str,
    model: str,
    temperature: float,
    prompt: str,
    stream: bool,
    verbose: bool,
    attach_files: Optional[str]
):
    """Send a prompt to the LLM and stream the response"""
    config = load_config()
    
    base_url = base_url or config.get('base_url')
    refresh_token = refresh_token or config.get('refresh_token')
    
    if not refresh_token:
        click.echo("Missing refresh token. Please run 'llm configure' or provide --refresh-token", err=True)
        sys.exit(1)
    
    async def run():
        async with LLMClient(
            base_url=base_url,
            refresh_token=refresh_token
        ) as client:
            request = ChatCompletionRequest(
                sessionId=notebook_id,
                message=prompt,
                params={
                    "model": model,
                    "temperature": temperature
                },
                fabFileIds=attach_files.split(',') if attach_files else []
            )

            try:
                await client.submit_prompt(request)
                async for event in client.stream_events():
                    if verbose and isinstance(event, StatusEvent):
                        print(event.status, flush=True)
                    if stream and isinstance(event, ContentEvent):
                        print(event.content, end="\r", flush=True)
                    if isinstance(event, CompletionEvent):
                        print(event.message, flush=True)
                        break
            except Exception as e:
                click.echo(f"Error: {str(e)}", err=True)
                sys.exit(1)

    asyncio.run(run())

def main():
    """Entry point for the CLI"""
    cli()

if __name__ == '__main__':
    main() 