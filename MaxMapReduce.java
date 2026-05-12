import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.*;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

class MaxMapper extends Mapper<LongWritable, Text, Text, IntWritable> {

    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {

        String valueStr = value.toString().trim();

        int number = Integer.parseInt(valueStr);

        context.write(new Text("max"), new IntWritable(number));
    }
}

class MaxReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        int maxSoFar =  Integer.MIN_VALUE;
        for(IntWritable value : values){
            if(value.get() > maxSoFar){
                maxSoFar = value.get();
            }
        }

        context.write(key , new IntWritable(maxSoFar) );
    }
}
/* 
class MinReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {

        int minSoFar =  Integer.MAX_VALUE;
        for(IntWritable value : values){
            if(value.get() < minSoFar){
                minSoFar = value.get();
            }
        }

        context.write(key , new IntWritable(minSoFar) );
    }
}*/


public class MaxMapReduce {

    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();

        Job job = Job.getInstance(conf, "Maximum value");

        job.setJarByClass(MaxMapReduce.class);

        job.setMapperClass(MaxMapper.class);
        job.setReducerClass(MaxReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);

    }
}