#function to split input and output cell
from IPython.display import display, HTML
def split_screen():
    identity = 'mycell'
    script = f'''
    let cell = this.closest('.code_cell');
    console.log('{identity}');
    cell.id = '{identity}';
    '''
    return display(HTML('''
    <img src onerror="%s">
    <style>
    #notebook-container {
       width: 95%%
    }
    #%s {
       flex-direction: row !important;
    }

    #%s .input {
        width: 50%%
    }

    #%s .output_wrapper {
        width: 50%%
    }
    }
    </style>
    '''%(script,identity,identity,identity)))