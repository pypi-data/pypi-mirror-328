
public class TestJavaParser {

    interface ILove {
        void foo();
        void love();
        default int testAdd(int x, int y) { return 0;}
    }

    class Love implements ILove {
        public void foo() {
            System.out.println("foo");
        }

        public void love() {
            System.out.println("love");
        }
    }

    public void testJavaParser() {

    }

    public int add(int x, int y) {
        return x + y;
    }

    private int a;
    private int b;
}
