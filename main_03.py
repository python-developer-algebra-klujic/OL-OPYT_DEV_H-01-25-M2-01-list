import os


text = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Sed lacinia lectus a tristique varius. Curabitur auctor sem sed luctus dapibus. 
Aliquam dui felis, pretium vel tellus vel, pretium suscipit elit. 
Maecenas placerat, justo ut congue feugiat, quam ante rutrum tortor, 
vitae aliquam tellus lorem a nunc. Ut scelerisque, mi non faucibus ullamcorper, 
lorem nibh dictum nunc, ut euismod nibh dolor nec urna. Donec lacinia sem augue, 
a mattis turpis pellentesque sed. 
Donec dapibus massa eget nulla tempus egestas non non magna. 
Curabitur et tortor ut tortor tincidunt imperdiet id vitae nunc. 
Nulla porttitor in massa a tincidunt. Donec tempor velit orci, 
sed efficitur lectus iaculis vel. Sed sollicitudin laoreet felis, 
vitae ultrices enim interdum vitae. Donec ornare lectus vitae nisi ultrices, 
sed vulputate ligula condimentum.

Aenean sed eros neque. Aenean vestibulum justo nec ex ornare congue. 
In tristique odio et leo suscipit, et consequat velit posuere. 
Vestibulum sit amet sapien pretium, rhoncus nunc non, malesuada dui. 
Fusce quam ligula, congue quis ornare vitae, placerat sed nunc. 
Quisque sed bibendum enim. Nullam blandit magna ac tempus rutrum. 
Cras porta, diam vitae accumsan pellentesque, velit nibh rhoncus diam, 
quis pellentesque nisl sapien in ex. Nulla facilisi. Ut at mauris sodales, 
faucibus tortor in, maximus nisl. Vivamus dictum pellentesque urna.

Proin et ultricies purus. Nulla auctor felis quis sem fermentum faucibus. 
Etiam vitae consectetur odio. Integer in egestas leo, lacinia facilisis sem. 
Suspendisse eget est at odio egestas pellentesque in nec felis. 
Integer vel cursus purus, vitae ultrices est. Donec eleifend facilisis tempor. 
Nam eget sem quam. Etiam ut quam in dui posuere eleifend. 
In ut tortor ac nisi rhoncus viverra. Etiam feugiat vel turpis at auctor.

Sed sit amet lacus eget tortor ornare elementum vitae quis ligula. 
Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 
Pellentesque id risus mattis, mattis sem quis, faucibus lectus. 
Nam vitae aliquet orci. Sed id scelerisque arcu, et convallis mauris. 
Nullam consectetur ante lorem. Vivamus consequat efficitur mauris, 
vel gravida odio dictum ut. Aenean tempus condimentum eros, 
nec lobortis nunc porta eget. Ut ultricies nisi vitae justo convallis, 
id euismod ipsum suscipit. Nulla erat lacus, placerat ac leo efficitur, 
gravida placerat magna. Integer sit amet felis dignissim dui commodo porta vel eu felis. 
Etiam nunc turpis, imperdiet at faucibus eu, dictum placerat mauris. 
Vivamus sit amet eleifend nibh, eu aliquam nisl. Aliquam pharetra cursus dapibus. 
Duis ut dictum ex, et pulvinar risus.

Donec fringilla sollicitudin eros, eget efficitur sem euismod eu. 
Nulla dapibus sapien elit, in aliquam nisi dignissim quis. 
Cras pharetra urna nisi, id consequat mauris gravida vitae. 
Etiam maximus nunc ut augue rutrum aliquam. Phasellus ligula diam, 
laoreet in auctor sit amet, mattis eget nibh. Ut id fermentum tortor. 
Vestibulum et porta metus, vitae sollicitudin lorem. 
Maecenas feugiat lorem eget dui vehicula, eu euismod justo ullamcorper. 
Curabitur nec justo et dolor iaculis congue eget ac nulla. 
Phasellus commodo maximus rutrum. Suspendisse potenti.
'''

# Procititi tekst prije obrade
# 1. nacin
# text = text.replace('.', '')
# text = text.replace(',', '')
# text = text.lower()

words = text.split() # Predefinirana vrijednost po kojoj se dijeli tekst na manje elemente je razmak
# print(words)

# words_counter = 0
# for word in words:
#     words_counter += 1
# words_count = len(words)
# print(f'U tekstu ima {words_count} rijeci.')

# search_word = input('Upisite rijec koju zelite prebrojati u tekstu: ')
# search_word_count = text.count(search_word)
# print(f'Rijec {search_word} se u tekstu pojavljuje {search_word_count} puta.')

# search_word = input('Upisite rijec koju zelite prebrojati u tekstu: ')
# search_word_count = 0
# for word in words:
#     if word.lower() == search_word.lower():
#         search_word_count += 1

# print(f'Rijec {search_word} se u tekstu pojavljuje {search_word_count} puta.')


# Procititi tekst prije obrade
# 2. nacin
for word in words:
    index = words.index(word)

    word = word.replace('.', '')
    word = word.replace(',', '')
    word = word.lower()

    words[index] = word



while True:
    os.system('cls')

    search_word = input('Upisite rijec koju zelite prebrojati u tekstu: ')
    search_word_count = 0
    for word in words:
        if word == search_word:
            search_word_count += 1

    print(f'Rijec {search_word} se u tekstu pojavljuje {search_word_count} puta.')
    print()

    next_word = input('Zelite li potraziti novu rijec? (da/ne): ')
    if next_word.lower() != 'da':
        break
