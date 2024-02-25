<div align="center">
  <img src="https://i.postimg.cc/W1F4WKJs/ICPC.png" alt="ICPC" width="120"/>
</div>

<br />

[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=1000&size=34&pause=1000&width=435&lines=WEEK+4)](https://git.io/typing-svg)

## About:
-  Sheet #4 (Strings)
-  Problems: A to V
-  Go to [click here](https://vjudge.net/contest/546316)
<br />

<br />
<hr />

## My Cpp Template
```cpp
#include <iostream>

#define endl "\n"

using namespace std;

void fastIO() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
}

int main() {
    fastIO();
    /* Your Code */
}
```
<br />

## Easy Start
- run ```makecpp [FileName]```
- Instructions:
    * create a file name ```makecpp```
    * Copy This bash Script:
    ```bash
    #!/bin/bash
    if [ $# -eq 0 ]; then
        echo "Usage: $0 <filename.cpp>"
        exit 1
        fi

    filename=$1
    filename="${filename%.*}.cpp"

    # Check if the file already exists
    if [ -e "$filename" ]; then
        echo "File already exists. Choose a different filename."
        exit 1
    fi

    # Create the C++ file with the template
    echo "#include <iostream>" > "$filename"
    echo "" >> "$filename"
    echo "#define endl \"\n\"" >> "$filename"
    echo "" >> "$filename"
    echo "using namespace std;" >> "$filename"
    echo "" >> "$filename"
    echo "void fastIO() {" >> "$filename"
    echo "    ios_base::sync_with_stdio(false);" >> "$filename"
    echo "    cin.tie(NULL);" >> "$filename"
    echo "    cout.tie(NULL);" >> "$filename"
    echo "}" >> "$filename"
    echo "" >> "$filename"
    echo "int main() {" >> "$filename"
    echo "    fastIO();" >> "$filename"
    echo "" >> "$filename"
    echo "}" >> "$filename"

    echo "C++ file created: $filename"
    ```

- add the parent folder to the path based on your operation system "google it if stuck"

<br />

## Authors :black_nib:

* __Yousef Bakier__ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
 &nbsp;&nbsp;[<img height="" src="https://img.shields.io/static/v1?label=&message=GitHub&color=181717&logo=GitHub&logoColor=f2f2f2&labelColor=2F333A" alt="Github">](https://github.com/Y-Baker)
