from figurasplanas.figuraplana import FiguraPlana

def test_init():
    fig = FiguraPlana(A=48.0, Ix=576.0, Iy=64.0, xc=0.0, yc=0.0, Ixy=0.0)
    assert fig.A == 48.0
    assert fig.rx == (576.0 / 48.0) ** 0.5