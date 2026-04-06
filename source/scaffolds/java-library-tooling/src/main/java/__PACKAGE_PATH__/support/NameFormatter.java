package __PACKAGE_NAME__.support;

public final class NameFormatter {

    private NameFormatter() {
    }

    public static String format(String input) {
        return "[tooling] " + input;
    }
}

