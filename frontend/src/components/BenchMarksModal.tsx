import { Box, Modal, Typography, IconButton } from "@mui/material";
import CommonTable, { type BenchmarkRow } from "./CommonTable";

const style = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "90%",
  maxWidth: 800,
  bgcolor: "background.paper",
  borderRadius: 2,
  boxShadow: 24,
  p: 3,
};

interface ModalProps {
  open: boolean;
  onClose: () => void;
  data: BenchmarkRow[];
}

export default function BenchMarksModal({ open, onClose, data }: ModalProps) {
  return (
    <Modal open={open} onClose={onClose}>
      <Box sx={style}>
        <Box sx={{ display: "flex", justifyContent: "space-between", mb: 2 }}>
          <Typography variant="h6">Local LLM Benchmark Comparison</Typography>
          <IconButton size="small" onClick={onClose}>✕</IconButton>
        </Box>
        <CommonTable data={data} />
      </Box>
    </Modal>
  );
}
