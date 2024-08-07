package HierarchyClustering;

import java.io.FileNotFoundException;
import java.io.IOException;
import java.util.Arrays;


public class HierarchyClustering {
    public static Node getDendogram(double[][] dataset) {
        int numCh = dataset[0].length;
        int dsLength = dataset.length;

        // Generate matrix distances
        double[][] distances = new double[dsLength][];
        for (int i = 1; i < dsLength; i++) {
            double[] distancesI = new double[i];
            for (int j = 0; j < i; j++) {
                double distance = 0.0;
                for (int ch_i = 0; ch_i < numCh; ch_i++) {
                    distance += Math.pow(dataset[i][ch_i]-dataset[j][ch_i], 2);
                }
                distancesI[j] = Math.sqrt(distance);
            }
            distances[i] = distancesI;
        }

        // Convert distances matrix into a flat array
        double[][] flatDistances = new double[getTotalDistances(dsLength)-dsLength][3];
        for (int i = 1, t = 0; i < dsLength; i++) {
            for (int j = 0; j < i; j++) {
                // Optimize the array created to store indexes as int
                flatDistances[t++] = new double[]{distances[i][j],i,j};
            }
        }
        // Sort the distances array
        Arrays.sort(flatDistances, (a,b) -> a[0] > b[0] ? 1 : -1);

        // Generate an array of leafts
        Leaf[] leafs = Arrays.stream(dataset).map(Leaf::new).toArray(Leaf[]::new);
        // Create the dendogram
        int t = 0;
        for (double[] item : flatDistances) {
            Node lParent = leafs[(int) item[1]].getLastParent();
            Node rParent = leafs[(int) item[2]].getLastParent();
            if (lParent != rParent) {
                Cluster parent = new Cluster(lParent, rParent, item[0]);
                lParent.parent = parent;
                rParent.parent = parent;
                if (++t >= dsLength-1)
                    return parent;
            }
        }

        return null;
    }

    public static int getTotalDistances(int size) {
        return size == 0 ? 0 : size + getTotalDistances(size - 1);
    }


    public static void main(String[] args) throws FileNotFoundException, IOException {
        Node dendogram = getDendogram(ReadDataset.ReadFile("HierarchyClustering/iris.data", 0, 4));
        System.out.println("end");
    }
}