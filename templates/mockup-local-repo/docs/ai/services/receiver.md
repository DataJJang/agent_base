# Receiver Rules

## 1. 적용 대상

- parser, decoder, ingress, publish 흐름을 가진 receiver 저장소

## 2. 구조 원칙

### 구성 원칙

- ingress 경계는 `controller` 또는 `tcp/handler`에 둔다.
- payload 해석은 `parser` 또는 `decoder`로 분리한다.
- 비즈니스 처리와 발행은 `service` 또는 publisher에서 수행한다.
- 설정과 연결 정보는 `config`에 둔다.
- 암호화, 공통 계산, 포맷 변환은 `common/util`에 둔다.

## 3. 수신 처리 규칙

- 수신 즉시 payload를 그대로 여기저기 전달하지 않는다.
- 먼저 parser 또는 decoder 단계에서 normalize 한다.
- normalize 이후 모델을 기준으로 검증한다.
- 발행 또는 저장 전에 필수 식별자와 유효성 검사를 수행한다.
- 처리 실패는 수신 실패, 파싱 실패, business 실패, 발행 실패로 나눠서 본다.

## 4. 프로토콜 처리 규칙

- MQTT topic, packet type, device identifier 같은 주요 키를 먼저 식별한다.
- 수신 경계와 business 처리 경계를 분리해 장애 분석이 가능하게 유지한다.
- idempotency가 필요한 수신은 중복 판단 기준을 서비스 레벨에서 유지한다.
- receiver는 API 서비스와 달리 연속 수신과 프로토콜 해석이 핵심이므로 handler와 parser를 얇게 유지하고 service를 중심으로 규칙을 모은다.

## 5. 운영 포인트

- ingress 수신량과 실패율
- parser 또는 decoder 오류
- publish 또는 저장 성공률
- 연속 수신 누락/중복 여부
- 프로토콜별 에러 패턴

## 6. 검증 기준

- 최소 `./gradlew compileJava` 또는 `./gradlew test`
- parsing, decoder, handler routing 로직을 우선 검토
- 실시간 수신 기능은 완전한 통합 테스트가 어려우면 compile + 핵심 parsing smoke를 최소선으로 본다

## 7. 체크리스트

- [ ] ingress 경계가 controller 또는 handler에만 머무르는가
- [ ] parser 또는 decoder가 payload normalize를 담당하는가
- [ ] business 검증과 발행 로직이 service에 있는가
- [ ] payload 전체 dump 로그를 남기지 않는가
- [ ] topic, packet type, device 식별자 로그 기준이 있는가
- [ ] compile 또는 test를 수행했는가
