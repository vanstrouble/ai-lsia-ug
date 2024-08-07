package HierarchyClustering;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;

import java.util.Arrays;

public class ReadDataset {
    public static double[][] ReadFile(String filePath, int startCol, int endCol) 
    throws FileNotFoundException, IOException {
        BufferedReader reader = new BufferedReader(new FileReader(new File(filePath)));

        double[][] dataset = reader.lines().map(l -> Arrays.stream(Arrays.copyOfRange(l.split(","),
            startCol, endCol)).mapToDouble(Double::parseDouble).toArray()).toArray(double[][]::new);
        reader.close();

        return dataset;
    }

    public static void main(String[] args) throws FileNotFoundException, IOException {
        ReadFile("HierarchyTree/iris.data", 0, 4);
    }
}
