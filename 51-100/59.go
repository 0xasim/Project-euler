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
  i := 0
  print(data)
  print("\nprinting data start\n")
	for i=0; i<3; i++ {
    print(data[i])
  }
  print("\nprinting data end")
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
func string2bin(s string) string {
  var binString string
  for _, c := range s {
    binString = fmt.Sprintf("%s%b", binString, c)
  }
  return binString
}
func bin2string(b []byte) string {
  var str string
  str = fmt.Sprintf("%x", b)
  // str = rune(b)
  return str
}
func xor(b1 byte, b2 byte) byte {
  if b1 != b2 { return 1 } 
  return 0
}
func decrypt(data []int, key string){
  bin_key := string2bin(key)
  print("\n"+key)
  print("\n"+bin_key)
  fmt.Printf("\n")
  var l int = 0
  // for o := range data {
  o := 0
  for o=0; o<=1; o++ {
    // bin_d1 := strconv.FormatInt(int64(data[o]), 2)
    bin_d1 := string2bin(string(data[o]))
    dLen := len(bin_d1)
    rbuffer := make([]byte, dLen)
    for p := range bin_d1 {
      bin_d2 := bin_d1[p]
      result := xor(bin_d2, bin_key[l])
      rbuffer[p] = result
      // fmt.Printf("%b,%b: %b\t", bin_d2, bin_key[l], result)
      l++
      if l > len(bin_key)-1 { l = 0 }
    }
    // sbuffer, _ := strconv.Atoi(string(rbuffer[:]))
    sbuffer := bin2string(rbuffer)
    fmt.Printf("data[o]: %d,\tbin_d1: %s,\trbuffer: %b,\tsbuffer: %s\n",
    data[o], bin_d1, rbuffer, sbuffer)
    Use(sbuffer)
  }
}
func main() {
	_ , data := readFile("/Users/dude/fun/project_euler/data/p059_cipher.txt")
  splitted := splitStr(data, []byte(",")[0])
  alph := "abcdefghijklmnopqrstuvwxyz"
  Use(splitted)
  decrypt(splitted, "abc")
  for u := range alph {
    for v := range alph {
      for w := range alph {
        t := string(alph[u])+string(alph[v])+string(alph[w])
        Use(t)
      }
    }
  }
}

