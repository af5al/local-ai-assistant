import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select, { type SelectChangeEvent } from "@mui/material/Select";

type InputParams = {
  label?: string;
  options: any[];
  value: string;
  onChange: (model: string) => void;
};

export default function SelectSmall({
  options,
  label = "Select a model",
  value,
  onChange,
}: InputParams) {
  const handleChange = (event: SelectChangeEvent) => {
    if (onChange) onChange(event.target.value);
  };

  return (
    <FormControl sx={{ m: 1, minWidth: 200 }} size="small">
      <InputLabel id="model-select-label">{label}</InputLabel>
      <Select
        labelId="model-select-label"
        id="model-select"
        value={value}
        label={label}
        onChange={handleChange}
      >
        {options?.map((op: string) => (
          <MenuItem key={op} value={op}>
            {op}
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
