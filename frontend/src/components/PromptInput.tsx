import {Autocomplete as AutoCompleteInput, TextField} from '@mui/material'

type PromptInputParams = {
    promptsHistory: any[];
    placeholder?: string;
} 

export const PromptInput = ({promptsHistory, placeholder}: PromptInputParams) => {
  return (
        <AutoCompleteInput
            disablePortal
            options={promptsHistory}
            sx={{ width: 300 }}
            renderInput={(params) => <TextField {...params} label={placeholder || "Ask something..."} />}
        />
  );
};
