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
  label,
  value,
  onChange,
}: InputParams) {
  const handleChange = (event: SelectChangeEvent) => {
    if (onChange) onChange(event.target.value);
  };

  return (
    <FormControl sx={{ m: 1, minWidth: 120 }} size="small">
      <InputLabel id="demo-select-small-label">
        {label || "select model"}
      </InputLabel>
      <Select
        labelId="demo-select-small-label"
        id="demo-select-small"
        value={value}
        label={label || "model"}
        onChange={handleChange}
      >
        {options?.map((op: string) => (
          <MenuItem key={op} value={op}>
            <em>{op}</em>
          </MenuItem>
        ))}
      </Select>
    </FormControl>
  );
}
