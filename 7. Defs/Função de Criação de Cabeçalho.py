def escreva(txt):
    print('━'*(len(txt)+4))
    print(f'{txt}'.center(len(txt)+4))
    print('━' * (len(txt) + 4))

# Output:
escreva('Teste')
escreva('Paralelepípedo')
escreva('Python')