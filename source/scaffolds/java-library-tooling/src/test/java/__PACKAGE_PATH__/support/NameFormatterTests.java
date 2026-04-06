package __PACKAGE_NAME__.support;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class NameFormatterTests {

    @Test
    void formatPrefixesValue() {
        assertEquals("[tooling] sample", NameFormatter.format("sample"));
    }
}
