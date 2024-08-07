package HierarchyClustering;

import java.util.Arrays;
import java.util.stream.Collectors;

public class Leaf extends Node {
    double[] chs;

    public Leaf(double[] chs) {
        this.chs = chs;
    }

    public double[] getchs() {
        return chs;
    }

    @Override
    public String toString() {
        return Arrays.stream(chs).mapToObj(String::valueOf).collect(Collectors.joining(", "));
    }

}
