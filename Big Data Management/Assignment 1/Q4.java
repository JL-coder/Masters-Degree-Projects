import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;
import java.util.HashSet;

public class Q4 {

    public static class CustomMapper
            extends Mapper<LongWritable, Text, IntWritable, Text> {
        private static HashMap<Integer, Integer> customerIdCCMap = new HashMap<>();

        protected void setup(Context context) throws IOException, InterruptedException {
            try {
                URI[] customerFile = context.getCacheFiles();
                if (customerFile != null && customerFile.length > 0) {
                    for (URI file : customerFile) {
                        readFile(file, context);
                    }
                }
            } catch (IOException ex) {
                ex.printStackTrace();
                System.exit(1);
            }
        }

        private void readFile(URI file, Context context) {
            try {
                FileSystem fs = FileSystem.get(context.getConfiguration());
                Path getFilePath = new Path(file.toString());
                BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(fs.open(getFilePath)));
                String value;
                String[] customerData;
                while ((value = bufferedReader.readLine()) != null) {
                    customerData = value.split(",");
                    customerIdCCMap.put(Integer.parseInt(customerData[0]), Integer.parseInt(customerData[4]));
                }
            } catch (Exception ex) {
                ex.printStackTrace();
                System.exit(1);
            }
        }

        public void map(LongWritable key, Text value, Context context
        ) throws IOException, InterruptedException {
            try {
                String[] transactionData = value.toString().split(",");
                context.write(new IntWritable(customerIdCCMap.get(Integer.parseInt(transactionData[1]))),
                        new Text(transactionData[1] + "," + transactionData[2]));

            } catch (Exception ex) {
                ex.printStackTrace();
                System.exit(1);
            }
        }
    }

    public static class CustomReducer
            extends Reducer<IntWritable, Text, IntWritable, Text> {

        public void reduce(IntWritable key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
            try {
                Float min = 1000000F, max = 0F, transVal;
                HashSet<Integer> customerSet = new HashSet<>();
                String[] listVals;
                for (Text val : values) {
                    listVals = val.toString().split(",");
                    customerSet.add(Integer.parseInt(listVals[0]));
                    transVal = Float.parseFloat(listVals[1]);
                    if (transVal < min)
                        min = transVal;
                    if (transVal > max)
                        max = transVal;
                }
                context.write(key, new Text(customerSet.size() + "," + min + "," + max));
            } catch (Exception ex) {
                ex.printStackTrace();
                System.exit(1);
            }
        }
    }


    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job j = Job.getInstance(conf, "Question 4");

        j.setJarByClass(Q4.class);
        j.setMapperClass(Q4.CustomMapper.class);
        j.setReducerClass(Q4.CustomReducer.class);

        //int writable/floatwritable
        //Added from previous version
        j.setMapOutputKeyClass(IntWritable.class);
        j.setMapOutputValueClass(FloatWritable.class);
        j.setOutputKeyClass(Text.class);
        j.setOutputValueClass(Text.class);
        //j.setJobName("Problem 4");

        //Try knocking this out?
        //Path cPath = new Path("http://localhost:9870/explorer.html#/cs585/project_1/Customers.csv");
        //j.addCacheFile(cPath.toUri());

        Path inPath = new Path(args[0]);
        Path outPath = new Path(args[1]);
        FileInputFormat.addInputPath(j, inPath);
        FileOutputFormat.setOutputPath(j, outPath);



        //String HADOOP_HOME = System.getenv("HADOOP_HOME");
        //Configuration conf = new Configuration();
        //conf.addResource(new Path(HADOOP_HOME + "/etc/hadoop/core-site.xml"));
        //conf.addResource(new Path(HADOOP_HOME + "/etc/hadoop/hdfs-site.xml"));
        //conf.set("mapreduce.output.textoutputformat.separator", ",");
        //FileSystem.get(conf).delete(new Path(args[2]), true);
        //Job job = Job.getInstance(conf, "query4");
        //job.setJarByClass(Q4.class);
        //job.setMapperClass(Q4.CustomMapper.class);
        //job.setReducerClass(Q4.CustomReducer.class);
        //job.setOutputKeyClass(IntWritable.class);
        //job.setOutputValueClass(Text.class);
        //job.addCacheFile(new Path(args[0]).toUri());
        //FileInputFormat.addInputPath(job, new Path(args[1]));
        //job.setOutputFormatClass(TextOutputFormat.class);
        //FileOutputFormat.setOutputPath(job, new Path(args[2]));
        //System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
