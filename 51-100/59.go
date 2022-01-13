package main
import (
	"os"
	"fmt"
)

func readFile(fname string) (int, []byte) {
	file, _ := os.Open(fname)
	fs, _ := file.Stat()
	data := make([]byte, fs.Size())
	count, _ := file.Read(data)
	return count, data
}

func splitStr(data string, delimiter string) {
	var oneVal string
	for i := 0; i < len(data); i++ {
		var iChar string = string(data[i])
		if delimiter == iChar {

		} else {
			oneVal += iChar
		}
	}
	fmt.Printf("%s\n%s%d\n", delimiter, data, len(data))
}

func main() {
	_ , data := readFile("/Users/dude/fun/project_euler/data/p059_cipher.txt")
	splitStr(string(data), ",")
}

