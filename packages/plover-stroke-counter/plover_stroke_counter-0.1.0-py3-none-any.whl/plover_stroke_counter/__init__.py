 from plover.meta import Meta

class StrokeCounter(Meta):
    def __init__(self):
        super().__init__()
        self.stroke_count = 0

    def on_stroke(self, stroke):
        self.stroke_count += 1
        print(f"Total strokes: {self.stroke_count}")

    def start(self, engine):
        engine.hook_connect("stroked", self.on_stroke)

    def stop(self, engine):
        engine.hook_disconnect("stroked", self.on_stroke)
