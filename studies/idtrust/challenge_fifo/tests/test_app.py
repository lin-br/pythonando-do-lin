from io import StringIO

import app

input_values = StringIO('10\n1 42\n2\n1 14\n3\n1 28\n3\n1 60\n1 78\n2\n2\n')


def test_should_the_ouput_equal_14_and_14(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', input_values)
    app.main()
    captured = capsys.readouterr()
    out = str(captured.out).replace('How many operations?', '').replace('Input the operation:', '').strip()
    assert out == '14\n14'
