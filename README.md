# AI-Based Assistive Vision System for Visually Impaired Individuals

## Overview

The AI-Based Assistive Vision System is a real-time computer vision and voice assistant application designed to help visually impaired individuals understand their surroundings.

The system uses deep learning-based object detection and natural language voice interaction to describe the environment and answer user questions in real time.

This project demonstrates practical implementation of:
- Computer Vision
- Deep Learning (YOLOv8)
- Speech Recognition
- Text-to-Speech Systems
- Real-Time AI Applications

---

## Key Features

### 1. Real-Time Object Detection
- Uses YOLOv8 for detecting objects from webcam feed.
- Identifies objects such as person, car, bus, chair, etc.
- Provides spoken description of surroundings.

### 2. Scene Understanding
- Generates natural summaries like:
  - "I can see a person in front of you."
  - "There is a car nearby."

### 3. Voice Interaction
- Press **L** to ask questions.
- Supports queries like:
  - "Is there anyone in front of me?"
  - "Is there a vehicle nearby?"
  - "What can you see?"

### 4. Smart Voice Output
- Avoids repeated announcements.
- Speaks only when scene changes or after fixed interval.
- Natural human-like response behavior.

---

## System Architecture

Camera Input → YOLOv8 Object Detection → Scene Analysis → Voice Response Engine

---
