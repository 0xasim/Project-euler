package main
import (
	"os"
	"fmt"
	"strconv"
	// "bytes"
	// "reflect"
)
func Use(vals ...interface{}) {
  for _, val := range vals {
    _ = val
  }
}

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
func stringToBin(s string) string {
  var binString string
  for _, c := range s {
    binString = fmt.Sprintf("%s%b", binString, c)
  }
  return binString
}
func xor(b1 byte, b2 byte) byte {
  if b1 != b2 {
    return 1
  } 
  return 0
}
func decrypt(data []int, key string){
  bin_key := stringToBin(key)
  var l int = 0
  for o := range data {
    bin_d1 := strconv.FormatInt(int64(data[o]), 2)
    for p := range bin_d1 {
      bin_d2 := bin_d1[p]
      result := xor(bin_d2, bin_key[l])
      fmt.Printf("%b,%b: %b\t", bin_d2, bin_key[l], result)
      l++
      if l > len(bin_key)-1 { l = 0 }
    }
    println()
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
        // t := alph[u]+alph[v]+alph[w]
        Use(v,w)
        fmt.Printf("%x ", alph[u])
        //decrypt(splitted, t)
      }
    }
  }
  Use(splitted)
}

