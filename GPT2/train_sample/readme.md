
# Sample train of gpt2

## Step1 prepare data

run `python /data/shakespeare/prepare.py`

get `train.bin`, `val.bin`

- train has 301,966 tokens
- val has 36,059 tokens

## step2 training
run `python train.py config/train_shakespeare_char_baby.py`

model save in `out-shakespeare-char/ckpt.pt`

## step3 generate
run `python sample.py`