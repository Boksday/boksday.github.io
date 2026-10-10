"""퍼즐 파일을 같은 모양으로 정리한다(그림 한 줄이 파일 한 줄). build.py가 부른다."""
import json


def dump_puzzle(puzzle):
    head = json.dumps({'id': puzzle['id'], 'name': puzzle['name'], 'palette': puzzle['palette']},
                      ensure_ascii=False, separators=(',', ':'))
    rows = ',\n'.join(f'  "{row}"' for row in puzzle['rows'])
    return head[:-1] + ',"rows":[\n' + rows + '\n]}\n'
