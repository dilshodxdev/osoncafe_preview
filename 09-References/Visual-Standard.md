# Vizual standart

## Dizayn tili

- Uslub: minimal, Swiss/grid-based, akademik va professional.
- Fon: `#FFFFFF`.
- Asosiy matn: `#17211D`.
- Asosiy yashil: `#0F7A55`.
- Yengil yashil: `#E8F5EE`.
- Chegara: `#CBD5D1`.
- Xato/xavf: `#B42318`.
- Ogohlantirish/Partial: `#B7791F`.
- Shrift: Inter; fallback — Arial, sans-serif.
- Gradient, 3D effekt, dekorativ soya va keraksiz ikonkalardan foydalanilmaydi.

## Holat semantikasi

| Holat | Ko‘rinish | Mazmuni |
|---|---|---|
| Implemented / Current | Yashil chiziq va yengil yashil fon | Kod/test dalili mavjud |
| Partial | Sariq-jigarrang chiziq, oq fon | Qisman mavjud yoki tashqi tekshiruv kerak |
| Proposed / Future | Kulrang uzilgan chiziq | Konsept yoki kelajak reja |
| External actor/system | Oqartirilgan kulrang blok | Tizim chegarasidan tashqarida |

## Diagramma qoidalari

1. Har bir diagrammada ID, nom, versiya va `Current`/`Proposed` yorlig‘i bo‘ladi.
2. Oqim odatda chapdan o‘ngga yoki yuqoridan pastga yuradi.
3. Bir xil domen obyektlari barcha diagrammalarda bir xil nomlanadi.
4. Bog‘lanishlar kesishishi minimallashtiriladi; ortogonal connector ishlatiladi.
5. Matn 12 px dan kichik bo‘lmaydi, kontrast kamida 4.5:1 bo‘ladi.
6. Har bir manba diagramma `.drawio` formatida tahrirlanadi va `.svg` hamda `.png`ga eksport qilinadi.
7. SVG asosiy vektor preview, PNG esa README/PDF va platformalararo moslik uchun ishlatiladi.
