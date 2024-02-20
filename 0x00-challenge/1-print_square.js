
#!/usr/bin/node
/*
    this display a square and the character #
    
    The program expects the size of the square as its initial argument 
    of the program.
*/


if (process.argv.length <= 2) {
    process.stderr.write("Missing argument\n");
    process.stderr.write("Usage: ./1-print_square.js <size>\n");
    process.stderr.write("Example: ./1-print_square.js 8\n");
    process.exit(1)
}

size = parseInt(process.argv[2], 10)

for (let m = 0 ; m < size ; m ++) {
    for (let p = 0 ; p < size ; p ++) {
        process.stdout.write("#");
    }
    process.stdout.write("\n");
}
