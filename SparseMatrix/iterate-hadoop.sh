#!/bin/sh
CONVERGE=1
rm v* log* m_out

$HADOOP_HOME/bin/hadoop dfsadmin -safemode leave
hdfs dfs -rm -r /output* 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
-mapper "/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/mapper_t1.py" \
-reducer "/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/reducer_t1.py '/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/v'"  \
-input "/input_${1}" \
-output /output1 #has sparse matrix

ITERATIONS=0

while [ "$CONVERGE" -ne 0 ]
do
	$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-*streaming*.jar \
	-mapper "/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/mapper_t2.py '/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/v'" \
	-reducer "/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/reducer_t2.py '/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/v1' '/home/roshan/Code/academics/sem5/BD/Assignment2_PageRank/SparseMatrix/m_out'" \
	-input /output1/part-00000 \
	-output /output2
	
	ITERATIONS=$((ITERATIONS + 1))

	CONVERGE=$(python3 check_conv.py >&1)
	hdfs dfs -rm -r /output2

	echo $CONVERGE
done

echo "Number of iterations = ${ITERATIONS}"