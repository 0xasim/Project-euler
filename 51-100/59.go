package main
import (
	"os"
	// "fmt"
	"strconv"
	// "bytes"
	// "reflect"
)

func readFile(fname string) (int, []byte) {
	file, _ := os.Open(fname)
	fs, _ := file.Stat()
	data := make([]byte, fs.Size())
	count, _ := file.Read(data)
	return count, data
}

func splitStr(data []byte, delimiter byte) []int {
  two_dim := make([]int, len(data)/2)
	var x int = 0
  var start int = 0
	for i := 0; i < len(data); i++ {
		if delimiter == data[i] {
      two_dim[x], _ = strconv.Atoi(string(data[start:i]))
			start = i+1
			x++
		}
	}
  two_dim[x], _ = strconv.Atoi(string(data[start:start+2]))
  return two_dim[:x+1]
}

func main() {
	_ , data := readFile("/Users/dude/fun/project_euler/data/p059_cipher.txt")
  splitted := splitStr(data, []byte(",")[0])
  println(splitted)
}

