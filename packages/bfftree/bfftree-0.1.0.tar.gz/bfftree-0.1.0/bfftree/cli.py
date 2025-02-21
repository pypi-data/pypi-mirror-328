import json
import pathlib
import typer
import lzma
import rich
from .bettertree_pb2 import RadixTreeNode as ProtoNode # type: ignore
from .tree import RadixTreeNode
from .inputs import (
    read_biostudies, remote_zip_to_bfftree, empiar_entry_to_bfftree,
    load_file_entries, build_radix_tree
)

app = typer.Typer()


@app.command()
def read_biostudies_cmd(json_path: str):
    """Read a BioStudies JSON file and print the number of entries and total size."""
    tree = read_biostudies(json_path)
    paths = tree.get_all_paths()
    typer.echo(f"Found {len(paths)} entries in {json_path}")
    typer.echo(f"Total size: {tree.get_size()} bytes")


@app.command()
def save_tree(json_path: str, output_path: str):
    """Read a BioStudies JSON file and save its radix tree structure."""
    entries = load_file_entries(json_path)
    tree = build_radix_tree(entries)
    tree.save_to_file(output_path)
    typer.echo(f"Saved radix tree to {output_path}")


@app.command()
def save_tree_proto(json_path: str, output_path: str):
    """Read a BioStudies JSON file and save its radix tree structure as protobuf."""
    entries = load_file_entries(json_path)
    tree = build_radix_tree(entries)
    tree.save_to_proto_file(output_path)
    typer.echo(f"Saved protobuf radix tree to {output_path}")


@app.command()
def read_tree_proto(proto_path: str):
    """Read a protobuf radix tree file and display statistics."""
    tree = RadixTreeNode.load_from_proto_file(proto_path)
    
    # Count total number of files (nodes with size > 0)
    def count_files(node: RadixTreeNode) -> int:
        count = 1 if node.size > 0 else 0
        for _, child in node.edges:
            count += count_files(child)
        return count
    
    num_files = count_files(tree)
    total_size = tree.get_size()
    
    typer.echo(f"Found {num_files} files in {proto_path}")
    typer.echo(f"Total size: {total_size} bytes")


@app.command()
def read_tree_proto_xz(proto_path: str):
    """Read an xz compressed protobuf radix tree file and display statistics."""
    proto_node = ProtoNode()
    with lzma.open(proto_path, 'rb') as f:
        proto_node.ParseFromString(f.read())
    
    tree = RadixTreeNode.load_from_proto_file_proto(proto_node)
    
    # Count total number of files (nodes with size > 0)
    def count_files(node: RadixTreeNode) -> int:
        count = 1 if node.size > 0 else 0
        for _, child in node.edges:
            count += count_files(child)
        return count
    
    num_files = count_files(tree)
    total_size = tree.get_size()
    
    typer.echo(f"Found {num_files} files in {proto_path}")
    typer.echo(f"Total size: {total_size} bytes")


@app.command()
def read_and_list(proto_path: str):
    """Read an xz compressed protobuf radix tree file and list all file paths."""
    proto_node = ProtoNode()
    with lzma.open(proto_path, 'rb') as f:
        proto_node.ParseFromString(f.read())
    
    tree = RadixTreeNode.load_from_proto_file_proto(proto_node)
    paths = tree.get_all_paths()
    
    # Sort paths by size (largest first)
    paths.sort(key=lambda x: x[1], reverse=True)
    
    for path, size in paths:
        typer.echo(f"{size:>12,} bytes  {path}")


@app.command()
def remote_zip_to_bfftree_cmd(zip_url: str, output_path: str):
    """Create a BFFTree from a remote zip file and save it as a protobuf file.
    
    Args:
        zip_url: URL of the zip file to process
        output_path: Path where to save the protobuf file
    """
    tree = remote_zip_to_bfftree(zip_url)
    
    # Save as compressed protobuf if output ends with .xz
    if output_path.endswith('.xz'):
        with lzma.open(output_path, 'wb') as f:
            f.write(tree.to_proto().SerializeToString())
    else:
        tree.save_to_proto_file(output_path)
    
    paths = tree.get_all_paths()
    typer.echo(f"Processed {len(paths)} files from {zip_url}")
    typer.echo(f"Saved protobuf radix tree to {output_path}")


@app.command()
def summarise(proto_path: str):
    """Summarize the contents of a BFFTree protobuf file.
    
    Prints:
    - Total number of files
    - Total size (human readable)
    - List of all file extensions present
    
    Args:
        proto_path: Path to the protobuf file (can be xz compressed)
    """
    # Load the tree
    if proto_path.endswith('.xz'):
        proto_node = ProtoNode()
        with lzma.open(proto_path, 'rb') as f:
            proto_node.ParseFromString(f.read())
        tree = RadixTreeNode.load_from_proto_file_proto(proto_node)
    else:
        tree = RadixTreeNode.load_from_proto_file(proto_path)
    
    # Get all paths and calculate statistics
    paths = tree.get_all_paths()
    total_files = len(paths)
    total_size = tree.get_size()
    
    # Calculate sizes by extension
    ext_sizes = {}
    for path, size in paths:
        ext = pathlib.Path(path).suffix.lower()
        if not ext:
            ext = "(no extension)"
        ext_sizes[ext] = ext_sizes.get(ext, 0) + size
    
    # Format size for human readability
    def human_size(size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.1f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.1f} PB"
    
    # Print summary
    console = rich.console.Console()
    console.print(f"\n[bold]Summary for {proto_path}:[/bold]\n")
    console.print(f"Total files: [cyan]{total_files:,}[/cyan]")
    console.print(f"Total size: [cyan]{human_size(total_size)}[/cyan] ({total_size:,} bytes)")
    
    if ext_sizes:
        # Create and populate table
        table = rich.table.Table(title="Files by Extension") # type: ignore
        table.add_column("Extension", style="green")
        table.add_column("File Count", justify="right", style="cyan")
        table.add_column("Total Size", justify="right", style="cyan")
        table.add_column("% of Total", justify="right", style="magenta")
        
        # Count files per extension
        ext_counts = {}
        for path, _ in paths:
            ext = pathlib.Path(path).suffix.lower()
            if not ext:
                ext = "(no extension)"
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
        
        # Add rows sorted by size (largest first)
        for ext, size in sorted(ext_sizes.items(), key=lambda x: x[1], reverse=True):
            count = ext_counts[ext]
            percentage = (size / total_size) * 100
            table.add_row(
                ext,
                f"{count:,}",
                human_size(size),
                f"{percentage:.1f}%"
            )
        
        console.print("\n")
        console.print(table)
    else:
        console.print("\n[yellow]No files found[/yellow]")


@app.command()
def empiar_entry_to_bfftree_cmd(
    accession_id: str,
    output_path: str = typer.Option(
        None,
        help="Output path for the protobuf file. If not provided, generates name like 'empiar-12105.pb.xz'"
    )
):
    """Create a BFFTree from an EMPIAR entry and save it as a protobuf file.
    
    Args:
        accession_id: EMPIAR accession ID (e.g. "EMPIAR-12105")
        output_path: Optional path where to save the protobuf file
    """
    # Generate default output path if none provided
    if output_path is None:
        # Extract number and create filename
        accession_no = accession_id.split('-')[-1]
        output_path = f"empiar-{accession_no}.pb.xz"
    
    tree = empiar_entry_to_bfftree(accession_id)
    
    # Save as compressed protobuf if output ends with .xz
    if output_path.endswith('.xz'):
        with lzma.open(output_path, 'wb') as f:
            f.write(tree.to_proto().SerializeToString())
    else:
        tree.save_to_proto_file(output_path)
    
    paths = tree.get_all_paths()
    typer.echo(f"Processed {len(paths)} files from {accession_id}")
    typer.echo(f"Saved protobuf radix tree to {output_path}")


if __name__ == "__main__":
    app()

