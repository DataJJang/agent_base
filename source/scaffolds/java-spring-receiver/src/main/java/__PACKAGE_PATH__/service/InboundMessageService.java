package __PACKAGE_NAME__.service;

import java.util.LinkedHashMap;
import java.util.Map;
import org.springframework.stereotype.Service;

@Service
public class InboundMessageService {

    public Map<String, Object> accept(String source, String messageId, String payload) {
        Map<String, Object> result = new LinkedHashMap<>();
        result.put("accepted", true);
        result.put("source", source);
        result.put("messageId", messageId);
        result.put("payloadLength", payload == null ? 0 : payload.length());
        return result;
    }
}

