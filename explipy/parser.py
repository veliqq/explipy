import traceback

def parse_traceback(tb):
    frames = []

    for frame_summary in traceback.extract_tb(tb):
        frames.append({
            "filename": frame_summary.filename,
            "lineno": frame_summary.lineno,
            "funcname": frame_summary.name,
            "code_line": frame_summary.line,
        })

    return frames
