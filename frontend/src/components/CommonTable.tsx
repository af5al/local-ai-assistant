import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Chip,
} from "@mui/material";

export interface BenchmarkRow {
  model: string;
  task_type: string;
  tokens: number;
  duration_sec: number;
  tps: number;
  ram_mb: number;
  valid_json: boolean;
}

export default function CommonTable({ data }: { data: BenchmarkRow[] }) {
  return (
    <TableContainer component={Paper} sx={{ maxHeight: 400 }}>
      <Table size="small" stickyHeader>
        <TableHead>
          <TableRow>
            <TableCell>
              <b>Model</b>
            </TableCell>
            <TableCell>
              <b>Task</b>
            </TableCell>
            <TableCell align="right">
              <b>Tokens/sec</b>
            </TableCell>
            <TableCell align="right">
              <b>Duration</b>
            </TableCell>
            <TableCell align="right">
              <b>RAM (MB)</b>
            </TableCell>
            <TableCell align="center">
              <b>Valid JSON</b>
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data?.map((row, index) => (
            <TableRow key={index} hover>
              <TableCell>{row.model}</TableCell>
              <TableCell>{row.task_type}</TableCell>
              <TableCell align="right">
                <b>{row.tps}</b>
              </TableCell>
              <TableCell align="right">{row.duration_sec}s</TableCell>
              <TableCell align="right">{row.ram_mb}</TableCell>
              <TableCell align="center">
                <Chip
                  size="small"
                  label={row.valid_json ? "Passed" : "Failed"}
                  color={row.valid_json ? "success" : "default"}
                />
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
