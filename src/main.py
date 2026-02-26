import cv2
import time
import speech_recognition as sr
from detection import ObjectDetector
from speech import Speaker


def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, phrase_time_limit=5)

    try:
        text = recognizer.recognize_google(audio)
        print("User said:", text)
        return text.lower()
    except:
        return ""


def generate_natural_summary(detected_objects):
    if not detected_objects:
        return "The environment looks clear."

    descriptions = []
    for obj, distance in detected_objects:
        descriptions.append(f"a {obj} {distance}")

    return "I can see " + ", ".join(descriptions) + "."


def answer_question(question, detected_objects):
    objects = {obj for obj, _ in detected_objects}

    if "anyone" in question or "person" in question:
        for obj, distance in detected_objects:
            if obj == "person":
                return f"Yes, there is a person {distance}."
        return "No person detected."

    if "vehicle" in question or "car" in question:
        for obj, distance in detected_objects:
            if obj in ["car", "bus", "truck"]:
                return f"Yes, a {obj} is {distance}."
        return "No vehicles nearby."

    if "what" in question:
        return generate_natural_summary(detected_objects)

    if detected_objects:
        return generate_natural_summary(detected_objects)

    return "I do not see anything clearly."


def main():
    detector = ObjectDetector()
    speaker = Speaker()

    cap = cv2.VideoCapture(0)

    last_spoken_scene = ""
    last_summary_time = 0
    summary_interval = 10  # seconds

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = detector.detect(frame)
        annotated_frame = results[0].plot()

        detected_objects = detector.extract_objects(results, frame.shape)

        current_scene = str(detected_objects)
        current_time = time.time()

        # Speak only if scene changes OR every 10 seconds
        if current_scene != last_spoken_scene or (current_time - last_summary_time > summary_interval):
            summary = generate_natural_summary(detected_objects)
            speaker.speak(summary)
            last_spoken_scene = current_scene
            last_summary_time = current_time

        cv2.imshow("AI Assistive Vision System", annotated_frame)

        key = cv2.waitKey(1) & 0xFF

        # Press L to ask question
        if key == ord("l"):
            question = listen()
            if question:
                answer = answer_question(question, detected_objects)
                print("Answer:", answer)
                speaker.speak(answer)
            else:
                speaker.speak("I did not understand your question.")

        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()