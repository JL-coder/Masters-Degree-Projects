import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.FloatWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

import javax.naming.Context;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URI;
import java.util.HashMap;

public class Q5 {
    public static class CustomMapper extends Mapper<LongWritable, Text, Text, FloatWritable> {
        private static HashMap<integer, String[]> ageAndGenderHMap = new HashMap<integer, String[]>();
        //comeup with better name!
        protected void setup(Context context) throws IOException, InterruptedException {
            try {
                URI[] customerFile = context.getCacheFiles();
                if (customerFile != null && customerFile.length > 0) {
                    for (URI file : customerFile)
                        readFile(file, context);
                }
            } catch (IOException ex) {
                ex.printStackTrace();
                System.exit(1);
            }
        }

        private int getAgeBucket(int age) {
            if (age >= 10 && age < 20)
                return 1;
            else if (age >= 20 && age < 30)
                return 2;
            else if (age >= 30 && age < 40)
                return 3;
            else if (age >= 40 && age < 50)
                return 4;
            else if (age >= 50 && age < 60)
                return 5;
            else if (age >= 60 && age <= 70)
                return 6;
            else return 0;
        }

    }
}
