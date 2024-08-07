package HierarchyClustering;

public class Node {
    Cluster parent = null;
    
    public Node getLastParent() {
        if (parent == null)
            return this;
        else
            return parent.getLastParent();

    }
}
