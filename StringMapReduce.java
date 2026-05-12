import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.Job;

import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;

class TokeinzerMapper extends Mapper<LongWritable, Text, Text, IntWritable> {
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();

        String[] words = line.split("\\s+");

        for (String word : words) {
            context.write(new Text(word), new IntWritable(1));
        }
    }
}

class IntegerReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {

        int sum = 0;

        for (IntWritable count : values) {
            sum += count.get();
        }
        context.write(key, new IntWritable(sum));

    }
}

/*class IntegerReducer extends Reducer<Text, IntWritable, Text, IntWritable> {
    
    private TreeMap<Integer, String> topMap = new TreeMap<>();
    private static final int N = 10; // Change this to your desired N

    @Override
    public void reduce(Text key, Iterable<IntWritable> values, Context context)
            throws IOException, InterruptedException {

        int sum = 0;
        for (IntWritable count : values) {
            sum += count.get();
        }

        topMap.put(sum, key.toString());

        if (topMap.size() > N) {
            topMap.remove(topMap.firstKey());
        }
    }

    @Override
    protected void cleanup(Context context) throws IOException, InterruptedException {
        for (Map.Entry<Integer, String> entry : topMap.entrySet()) {
            context.write(new Text(entry.getValue()), new IntWritable(entry.getKey()));
        }
    }
}*/

public class StringMapReduce {
    public static void main(String[] args) throws Exception {
        Configuration configuration = new Configuration();

        Job job = org.apache.hadoop.mapreduce.Job.getInstance(configuration, "Word Count");

        job.setJarByClass(StringMapReduce.class);

        job.setMapperClass(TokeinzerMapper.class);
        job.setReducerClass(IntegerReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));
        FileOutputFormat.setOutputPath(job, new Path(args[1]));

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}