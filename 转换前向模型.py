import subprocess

trained_model_path = 'models\\trained_models_voc2007\\resnet50_csv_.h5'
inference_model_path = 'models\\inference_models_voc2007\\retinanet_inference.h5'

convert_command = [
    'python',
    'keras-retinanet\\keras_retinanet\\bin\\convert_model.py',
    '--no-class-specific-filter',trained_model_path,inference_model_path,]

print('开始模型转换.')
process = subprocess.Popen(convert_command)
process.wait()
if process.returncode != 0:
    print(f'模型转换失败,失败码：{process.returncode}')
else:
    print("模型转换成功.")