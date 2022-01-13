package main
import (
	"os"
	"fmt"
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
  x, start := 0, 0
	for i := range data {
		if delimiter == data[i] {
      two_dim[x], _ = strconv.Atoi(string(data[start:i]))
			start = i+1
			x++
		}
	}
  two_dim[x], _ = strconv.Atoi(string(data[start:start+2]))
  return two_dim[:x+1]
}

func xor(data []int, key string){
  for o := range data {
    t := strconv.FormatInt(int64(data[o]), 2)
    fmt.Printf("%s,", t)
  }
}

func main() {
	_ , data := readFile("/Users/dude/fun/project_euler/data/p059_cipher.txt")
  splitted := splitStr(data, []byte(",")[0])
  alph := "abcdefghijklmnopqrstuvwxyz"
  println(alph)
  for u := range alph {
    for v := range alph {
      for w := range alph {
        println(u+v+w)
      }
    }
  }
  xor(splitted, "asd")
}

