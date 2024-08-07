package HierarchyClustering;

public class Cluster extends Node {
    private Node lChild;
    private Node rChild;
    private double distance;

    public Cluster(Node lChild, Node rChild, double distance) {
        this.lChild = lChild;
        this.rChild = rChild;
        this.distance = distance;
    }

    public Node getLChild() {
        return lChild;
    }

    public Node getRChild() {
        return rChild;
    }

    public double getDistance() {
        return distance;
    }
}
