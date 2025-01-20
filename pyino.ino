/* Pyino Tool 2025, webbrowser11 */
/* Run Python Code From Your Arduino. */

void setup() {
    Serial.begin(9600);
    Serial.println("run_python_code");
}

void loop() {
    if (Serial.avalible() > 0) {
        String response = Serial.readString();
        Serial.pritln(response)
    }
}
