# page-rank

An implemenation of the PageRank algorithm using the MapReduce model in Hadoop

## Dependencies

- `Hadoop 3.2.x`
- `Python 3.6` and later

## Usage

Clone this repository:

```zsh
git clone https://github.com/roshan-d21/page-rank.git
```

Start Hadoop

```zsh
$HADOOP_HOME/sbin/start-all.sh
```

Move the [SNAP](http://snap.stanford.edu/data/web-Google.html) dataset into `hdfs`

```zsh
cd page-rank
$HADOOP_HOME/bin/hdfs dfs -put ./web-Google.txt /input_SNAP
```

Pick one of the implementations and `cd` into the corresponding directory:

```zsh
cd AdjacencyList
```

OR

```zsh
cd SparseMatrix
```

Configure _file paths_ in `iterate-hadoop.sh`

Configure the _convergence_ value in `check_conv.py`

Give necessary file permissions using:

```zsh
chmod 755 -R .
```

Finally, execute the script using:

```zsh
sh iterate-hadoop.sh SNAP
```

## Output

The PageRank calculated for each node is stored in the file `v`
